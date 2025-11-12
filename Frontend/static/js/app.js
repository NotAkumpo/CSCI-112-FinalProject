/**
 * Game Store UI Controller
 * Manages filtering, searching, and displaying games from the backend API
 */

// Game data cache - stores all games fetched from API and current filtered results
let allGames = [];
let filteredGames = [];

// DOM element references for the filter controls and game display
const searchInput = document.getElementById('searchInput');
const minRatingSlider = document.getElementById('minRating');
const maxPriceSlider = document.getElementById('maxPrice');
const ratingValue = document.getElementById('ratingValue');
const priceValue = document.getElementById('priceValue');
const resetBtn = document.getElementById('resetBtn');
const gamesList = document.getElementById('gamesList');
const loadingSpinner = document.getElementById('loadingSpinner');
const noResults = document.getElementById('noResults');
const gameModal = document.getElementById('gameModal');
const closeBtn = document.querySelector('.close');
const gameDetails = document.getElementById('gameDetails');

// Attach event listeners for filter interactions - re-filters games on input
searchInput.addEventListener('input', filterGames);
minRatingSlider.addEventListener('input', () => {
    // Update displayed rating value as user moves slider
    ratingValue.textContent = minRatingSlider.value;
    filterGames();
});
maxPriceSlider.addEventListener('input', () => {
    // Update displayed price value as user moves slider
    priceValue.textContent = maxPriceSlider.value;
    filterGames();
});
resetBtn.addEventListener('click', resetFilters);
closeBtn.addEventListener('click', closeModal);
// Close modal when user clicks outside of modal content
window.addEventListener('click', (e) => {
    if (e.target == gameModal) closeModal();
});

// Load games from API when page finishes loading
document.addEventListener('DOMContentLoaded', loadGames);
/**
 * Fetch all games from the API and initialize the game list
 * Displays loading spinner while fetching, handles errors gracefully
 */
async function loadGames() {
    try {
        loadingSpinner.style.display = 'block';
        gamesList.innerHTML = '';

        const response = await fetch('/api/games');
        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        allGames = data.games;
        filterGames();
    } catch (error) {
        console.error('Error loading games:', error);
        // Display error message to user (text only, no user data to prevent XSS)
        loadingSpinner.innerHTML = `<div style="color: red;">Error loading games. Please try again later.</div>`;
    }
}

/**
 * Filter games based on search input and slider values
 * Searches game titles and developer names, filters by minimum rating and maximum price
 */
function filterGames() {
    const search = searchInput.value.toLowerCase();
    const minRating = parseInt(minRatingSlider.value);
    const maxPrice = parseInt(maxPriceSlider.value);

    // Filter games matching search criteria and price/rating constraints
    filteredGames = allGames.filter(game => {
        const title = (game.gameTitle || '').toLowerCase();
        const developer = (game.developer || '').toLowerCase();
        const rating = parseFloat(game.averageRating || 0);
        const price = parseFloat(game.currentPricePeso || 0);

        return (title.includes(search) || developer.includes(search)) &&
               rating >= minRating &&
               price <= maxPrice;
    });

    renderGames();
}

/**
 * Render the filtered game list to the DOM
 * Creates game cards for each filtered game and attaches click handlers
 */
function renderGames() {
    loadingSpinner.style.display = 'none';

    if (filteredGames.length === 0) {
        gamesList.innerHTML = '';
        noResults.style.display = 'block';
        return;
    }

    noResults.style.display = 'none';
    // Generate HTML for each filtered game and inject into DOM
    gamesList.innerHTML = filteredGames.map(game => createGameCard(game)).join('');

    // Attach click event listeners to each game card for opening detail modal
    document.querySelectorAll('.game-card').forEach((card, index) => {
        card.addEventListener('click', () => showGameDetails(filteredGames[index]));
    });
}

/**
 * Build HTML for a single game card
 * Includes game title, developer, rating, price, badges, and description preview
 */
function createGameCard(game) {
    const rating = parseFloat(game.averageRating || 0);
    // Convert numeric rating to star display (divide by 20 for 5-star scale)
    const stars = rating > 0 ? '⭐'.repeat(Math.floor(rating / 20)) : 'No ratings';
    // Show only first 3 categories to keep card compact
    const categories = (game.categories || []).slice(0, 3).map(cat => `<span class="category-tag">${cat}</span>`).join('');

    // Build array of special status badges
    const badges = [];
    if (game.isFree) badges.push('<span class="badge free">FREE</span>');
    if (game.isDiscounted) badges.push(`<span class="badge discount">-${game.currentDiscountPercent}%</span>`);
    if (game.isEarlyAccess) badges.push('<span class="badge early-access">EARLY ACCESS</span>');

    // Truncate description to 100 characters for preview
    const description = (game.description || '').substring(0, 100) + '...';

    return `
        <div class="game-card">
            <div class="game-card-header">
                <h2>${game.gameTitle || 'Unknown'}</h2>
            </div>
            <div class="game-card-body">
                <p class="game-developer">by ${game.developer || 'Unknown'}</p>

                <div class="game-rating">
                    <span class="rating-stars">${stars}</span>
                    <span class="rating-value">${rating}/100</span>
                </div>

                <div class="game-price">
                    ₱${parseFloat(game.currentPricePeso || 0).toFixed(2)}
                </div>

                <div class="price-info">
                    ${badges.join('')}
                </div>

                <div class="game-categories">
                    ${categories}
                </div>

                <p class="game-description">${description}</p>

                <button class="view-details-btn">View Details</button>
            </div>
        </div>
    `;
}

/**
 * Display full game details in a modal popup
 * Shows all game information including rating, price, categories, and system requirements
 */
function showGameDetails(game) {
    const rating = parseFloat(game.averageRating || 0);
    const stars = rating > 0 ? '⭐'.repeat(Math.floor(rating / 20)) : 'No ratings';
    // Parse and format release date for display
    const releaseDate = new Date(game.releaseDate).toLocaleDateString();
    // Show all categories in detail view (unlike card which shows only 3)
    const categories = (game.categories || []).map(cat => `<span class="category-tag">${cat}</span>`).join('');

    // Build special status badges for detail view
    const badges = [];
    if (game.isFree) badges.push('<span class="badge free">FREE</span>');
    if (game.isDiscounted) badges.push(`<span class="badge discount">-${game.currentDiscountPercent}% OFF</span>`);
    if (game.isEarlyAccess) badges.push('<span class="badge early-access">EARLY ACCESS</span>');

    gameDetails.innerHTML = `
        <div class="detail-header">
            <h1>${game.gameTitle || 'Unknown'}</h1>
            <p class="detail-developer">by ${game.developer || 'Unknown'}</p>
        </div>

        <div class="detail-section">
            <h3>Rating & Price</h3>
            <p>
                <strong>Rating:</strong> ${stars} ${rating}/100 (${game.reviewVerdict || 'No verdict'})<br>
                <strong>Price:</strong> ₱${parseFloat(game.currentPricePeso || 0).toFixed(2)}
                ${game.originalPricePeso && game.originalPricePeso !== game.currentPricePeso ? `<br><strike>₱${parseFloat(game.originalPricePeso).toFixed(2)}</strike>` : ''}
            </p>
            <div style="margin-top: 10px;">
                ${badges.join('')}
            </div>
        </div>

        <div class="detail-section">
            <h3>Release Date</h3>
            <p>${releaseDate}</p>
        </div>

        <div class="detail-section">
            <h3>Categories</h3>
            <div class="game-categories">
                ${categories}
            </div>
        </div>

        <div class="detail-section">
            <h3>Description</h3>
            <p>${game.description || 'No description available'}</p>
        </div>

        ${game.spaceRequiredGB ? `
        <div class="detail-section">
            <h3>System Requirements</h3>
            <p><strong>Storage:</strong> ${game.spaceRequiredGB} GB</p>
        </div>
        ` : ''}

        <div style="text-align: center; margin-top: 30px;">
            <button style="
                padding: 12px 30px;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 1.1em;
                font-weight: 600;
                cursor: pointer;
                transition: background 0.3s;
            " onmouseover="this.style.background='#764ba2'" onmouseout="this.style.background='#667eea'">
                Add to Cart
            </button>
        </div>
    `;

    // Display the modal with game details
    gameModal.style.display = 'block';
}

/**
 * Close the game details modal
 */
function closeModal() {
    gameModal.style.display = 'none';
}

/**
 * Reset all filter controls to default values and re-render the full game list
 */
function resetFilters() {
    // Clear search input
    searchInput.value = '';
    // Reset sliders to default bounds (0-5000 peso range)
    minRatingSlider.value = 0;
    maxPriceSlider.value = 5000;
    // Update displayed values to match slider positions
    ratingValue.textContent = '0';
    priceValue.textContent = '5000';
    // Trigger filter to show all games matching default criteria
    filterGames();
}
