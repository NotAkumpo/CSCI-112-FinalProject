"""
Game Store Backend Application
Flask application serving a game store with user authentication, game catalog,
and purchase/refund management using MongoDB.
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
import hashlib

# Add parent directory to path to import database modules
sys.path.insert(0, str(Path(__file__).parent.parent))

# Initialize Flask app with Frontend template and static file directories
app = Flask(__name__,
            template_folder='../Frontend/templates',
            static_folder='../Frontend/static')

# Configure session security - set SECRET_KEY in production environment variables
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
app.permanent_session_lifetime = timedelta(days=7)

# MongoDB connection to local database
try:
    conn = MongoClient('localhost', 27017)
    db = conn['finalProjectTest']
    print("Connected to MongoDB")
except Exception as e:
    print(f"✗ MongoDB connection failed: {e}")
    db = None

# ========================= HELPER FUNCTIONS =========================

def get_current_user():
    """
    Retrieve the currently authenticated user from the session.
    Returns user document from MongoDB or None if not authenticated.
    """
    if 'user_id' in session:
        try:
            user = db['customerAccounts'].find_one({
                "_id": ObjectId(session['user_id'])
            })
            return user
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
    return None

def hash_password(password):
    """
    Hash a plaintext password using SHA-256 algorithm.
    Used for both password creation and verification.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def validate_password(stored_hash, password):
    """
    Verify that a plaintext password matches its stored hash.
    Returns True if password is valid, False otherwise.
    """
    return stored_hash == hash_password(password)

# ========================= AUTH ROUTES =========================

@app.route('/')
def index():
    """Serve the main landing page"""
    current_user = get_current_user()
    if current_user:
        return redirect(url_for('store'))
    return render_template('login.html', current_page='login', current_user=None)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration (GET displays form, POST creates new account).
    Validates input, checks for duplicate username/email, and creates user document.
    """
    current_user = get_current_user()

    if request.method == 'POST':
        try:
            # Extract and sanitize form data
            username = request.form.get('username', '').strip()
            email = request.form.get('email', '').strip()
            first_name = request.form.get('first_name', '').strip()
            last_name = request.form.get('last_name', '').strip()
            country = request.form.get('country', '').strip()
            age = int(request.form.get('age', 0))
            phone = request.form.get('phone', '').strip()
            password = request.form.get('password', '')
            confirm_password = request.form.get('confirm_password', '')

            # Validate all required fields are provided
            if not all([username, email, first_name, last_name, country, age, phone, password]):
                flash('All fields are required', 'error')
                return redirect(url_for('register'))

            # Enforce minimum age requirement
            if age < 13:
                flash('You must be at least 13 years old', 'error')
                return redirect(url_for('register'))

            # Verify password confirmation matches
            if password != confirm_password:
                flash('Passwords do not match', 'error')
                return redirect(url_for('register'))

            # Enforce minimum password length
            if len(password) < 8:
                flash('Password must be at least 8 characters', 'error')
                return redirect(url_for('register'))

            # Check for duplicate username
            if db['customerAccounts'].find_one({'username': username}):
                flash('Username already taken', 'error')
                return redirect(url_for('register'))

            # Check for duplicate email
            if db['customerAccounts'].find_one({'emailAddress': email}):
                flash('Email already registered', 'error')
                return redirect(url_for('register'))

            # Hash password for secure storage
            password_hash = hash_password(password)

            # Create user document with all account information
            new_user = {
                'username': username,
                'password': password_hash,
                'customerFirstName': first_name,
                'customerLastName': last_name,
                'country': country,
                'emailAddress': email,
                'age': age,
                'birthDate': datetime.now(),
                'phoneNumber': phone,
                'walletBalancePeso': 0.0,
                'createdAt': datetime.now()
            }

            # Insert new user into database and get the generated ID
            result = db['customerAccounts'].insert_one(new_user)

            # Create session for newly registered user (auto-login)
            session.permanent = True
            session['user_id'] = str(result.inserted_id)

            flash('Account created successfully! Welcome to GameStore!', 'success')
            return redirect(url_for('store'))

        except ValueError as e:
            flash(f'Invalid input: {str(e)}', 'error')
            return redirect(url_for('register'))
        except Exception as e:
            flash(f'Registration error: {str(e)}', 'error')
            return redirect(url_for('register'))

    return render_template('register.html', current_page='register', current_user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login (GET displays form, POST authenticates user).
    Validates credentials and creates session if successful.
    """
    current_user = get_current_user()

    # Redirect to store if already logged in
    if current_user:
        return redirect(url_for('store'))

    if request.method == 'POST':
        try:
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '')
            remember = request.form.get('remember')

            # Validate required fields
            if not username or not password:
                flash('Username and password required', 'error')
                return render_template('login.html', current_page='login', current_user=None)

            # Query user by username
            user = db['customerAccounts'].find_one({'username': username})

            # Verify user exists and password is correct
            if not user or not validate_password(user['password'], password):
                flash('Invalid username or password', 'error')
                return render_template('login.html', current_page='login', current_user=None)

            # Create persistent session if "remember me" checkbox is checked
            session.permanent = remember is not None and remember.lower() != 'false'
            session['user_id'] = str(user['_id'])

            flash(f'Welcome back, {user["username"]}!', 'success')
            return redirect(url_for('store'))

        except Exception as e:
            flash(f'Login error: {str(e)}', 'error')
            return render_template('login.html', current_page='login', current_user=None)

    return render_template('login.html', current_page='login', current_user=current_user)

@app.route('/logout')
def logout():
    """
    Clear user session and log them out.
    """
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))

# ========================= PAGE ROUTES =========================

@app.route('/store')
def store():
    """
    Display the game store/catalog page (requires authentication).
    Lists all available games for purchase.
    """
    current_user = get_current_user()
    # Redirect to login if not authenticated
    if not current_user:
        return redirect(url_for('login'))

    # Add wallet balance to template context for display in UI
    if current_user:
        current_user['wallet_balance'] = current_user.get('walletBalancePeso', 0)

    return render_template('store.html',
                         current_page='store',
                         current_user=current_user)

@app.route('/library')
def library():
    """
    Display the user's owned game library (requires authentication).
    Shows all games the user has purchased.
    """
    current_user = get_current_user()
    # Redirect to login if not authenticated
    if not current_user:
        return redirect(url_for('login'))

    # Add wallet balance to template context for display in UI
    if current_user:
        current_user['wallet_balance'] = current_user.get('walletBalancePeso', 0)

    return render_template('library.html',
                         current_page='library',
                         current_user=current_user)

@app.route('/game/<game_id>')
def game_detail(game_id):
    """
    Display detailed information for a specific game (requires authentication).
    Shows game description, reviews, system requirements, and purchase options.
    """
    current_user = get_current_user()
    # Redirect to login if not authenticated
    if not current_user:
        return redirect(url_for('login'))

    # Add wallet balance to template context for display in UI
    if current_user:
        current_user['wallet_balance'] = current_user.get('walletBalancePeso', 0)

    try:
        # Validate that game_id is a valid MongoDB ObjectId
        if not ObjectId.is_valid(game_id):
            flash('Invalid game ID', 'error')
            return redirect(url_for('store'))

        # Query game from database, excluding placeholder entries
        game = db['storeGameInfo'].find_one({
            '_id': ObjectId(game_id),
            'gameTitle': {'$ne': 'String'}
        })

        if not game:
            flash('Game not found', 'error')
            return redirect(url_for('store'))

        # Fetch recent reviews for this game (limited to 5)
        reviews = list(db['gameReviews'].find({
            'gameTitle': game.get('gameTitle')
        }).limit(5))

        return render_template('game.html',
                             current_page='game',
                             current_user=current_user,
                             game=game,
                             reviews=reviews)
    except Exception as e:
        flash(f'Error loading game: {str(e)}', 'error')
        return redirect(url_for('store'))

# ========================= API ENDPOINTS =========================

@app.route('/api/games', methods=['GET'])
def api_get_games():
    """
    API endpoint to retrieve all games with optional filtering.
    Supports search, minimum rating, and maximum price filters.
    Query params: search, min_rating, max_price
    """
    try:
        # Extract search query and convert to lowercase for case-insensitive matching
        search = request.args.get('search', '').lower()

        # Parse and validate minimum rating filter (default 0)
        try:
            min_rating = float(request.args.get('min_rating', 0))
            if min_rating != min_rating:  # NaN check using identity comparison
                min_rating = 0
        except (ValueError, TypeError):
            min_rating = 0

        # Parse and validate maximum price filter (default 20000 pesos)
        try:
            max_price = float(request.args.get('max_price', 20000))
            if max_price != max_price:  # NaN check using identity comparison
                max_price = 20000
        except (ValueError, TypeError):
            max_price = 20000

        # Fetch all games with valid data from database (exclude placeholders)
        games = list(db['storeGameInfo'].find({
            "gameTitle": {"$ne": "String"},
            "averageRating": {"$type": ["int", "double", "decimal"]}
        }))

        # Apply filters to games in Python (client-side filtering for flexibility)
        filtered_games = []
        for game in games:
            try:
                title = game.get('gameTitle', '').lower()
                developer = game.get('developer', '').lower()
                rating = float(game.get('averageRating', 0))
                price = float(game.get('currentPricePeso', 0))

                # Check if game matches all filter criteria
                if (search in title or search in developer) and \
                   rating >= min_rating and \
                   price <= max_price:
                    # Convert MongoDB ObjectId to string for JSON serialization
                    game['_id'] = str(game['_id'])
                    filtered_games.append(game)
            except (ValueError, TypeError):
                # Skip games with invalid/missing data to prevent crashes
                continue

        return jsonify({'games': filtered_games, 'count': len(filtered_games)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/games/<game_id>', methods=['GET'])
def api_get_game_details(game_id):
    """
    API endpoint to retrieve full details for a specific game by ID.
    Returns complete game information including description, requirements, etc.
    """
    try:
        # Validate that game_id is a valid MongoDB ObjectId format
        if not ObjectId.is_valid(game_id):
            return jsonify({'error': 'Invalid game ID format'}), 400

        # Query specific game with valid rating data
        game = db['storeGameInfo'].find_one({
            "_id": ObjectId(game_id),
            "averageRating": {"$type": ["int", "double", "decimal"]}
        })

        if not game:
            return jsonify({'error': 'Game not found'}), 404

        # Convert ObjectId to string for JSON serialization
        game['_id'] = str(game['_id'])
        return jsonify(game)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/library', methods=['GET'])
def api_get_user_library():
    """
    API endpoint to retrieve the authenticated user's owned games.
    Returns list of all games the user has purchased.
    """
    try:
        # Verify user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Not authenticated'}), 401

        # Fetch all games owned by current user
        owned_games = list(db['ownedGameInfo'].find({
            'ownerUsername': current_user['username']
        }))

        # Enrich each owned game with developer info from store database
        for game in owned_games:
            game['_id'] = str(game['_id'])
            # Look up developer name and ID from store game info
            store_game = db['storeGameInfo'].find_one({'gameTitle': game['gameTitle']})
            if store_game:
                game['developer'] = store_game.get('developer', 'Unknown Developer')
                # Ensure game_id is set to the store game's _id for navigation
                game['game_id'] = str(store_game['_id'])
            else:
                game['developer'] = 'Unknown Developer'

        return jsonify({'games': owned_games, 'count': len(owned_games)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/profile', methods=['GET'])
def api_get_user_profile():
    """
    API endpoint to retrieve the authenticated user's profile information.
    Excludes sensitive data like password hashes.
    """
    try:
        # Verify user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Not authenticated'}), 401

        # Build safe user profile object (exclude password hash)
        user_data = {
            'id': str(current_user['_id']),
            'username': current_user.get('username'),
            'email': current_user.get('emailAddress'),
            'firstName': current_user.get('customerFirstName'),
            'lastName': current_user.get('customerLastName'),
            'walletBalance': current_user.get('walletBalancePeso', 0),
            'country': current_user.get('country'),
            'age': current_user.get('age')
        }

        return jsonify(user_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/purchase', methods=['POST'])
def api_purchase_game():
    """
    API endpoint to handle game purchases.
    Validates user has sufficient funds, creates owned game record, and updates wallet.
    Request JSON: {game_id: <ObjectId>}
    """
    try:
        # Verify user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Not authenticated'}), 401

        data = request.get_json()
        game_id = data.get('game_id')

        # Validate game_id is provided and is valid MongoDB ObjectId
        if not game_id or not ObjectId.is_valid(game_id):
            return jsonify({'error': 'Invalid game ID'}), 400

        # Retrieve game from store
        game = db['storeGameInfo'].find_one({'_id': ObjectId(game_id)})
        if not game:
            return jsonify({'error': 'Game not found'}), 404

        # Check if user already owns this game (prevent duplicate purchases)
        existing = db['ownedGameInfo'].find_one({
            'ownerUsername': current_user['username'],
            'gameTitle': game['gameTitle']
        })
        if existing:
            return jsonify({'error': 'You already own this game'}), 400

        # Get game price and user wallet balance
        price = game.get('currentPricePeso', 0)
        wallet = current_user.get('walletBalancePeso', 0)

        # Validate user has sufficient funds
        if wallet < price:
            return jsonify({'error': 'Insufficient wallet balance'}), 400

        # Create owned game record with unique license ID
        owned_game = {
            'ownerUsername': current_user['username'],
            'owner_id': str(current_user['_id']),
            'gameTitle': game['gameTitle'],
            'game_id': game_id,
            # Generate unique license ID using SHA-256 hash
            'licenseID': hashlib.sha256(f"{current_user['_id']}{game_id}{datetime.now()}".encode()).hexdigest(),
            'hoursPlayed': 0,
            'spaceRequiredGB': game.get('spaceRequiredGB', 0),
            'isInstalled': False,
            'datePurchased': datetime.now()
        }

        # Create transaction record for audit trail
        transaction = {
            'customerUsername': current_user['username'],
            'customer_id': str(current_user['_id']),
            'transactionDate': datetime.now(),
            'isRefund': False,
            'subtotal': price,
            'lineItems': [{
                'gameTitle': game['gameTitle'],
                'game_id': game_id,
                'purchasePricePeso': price,
                'isDiscounted': game.get('isDiscounted', False)
            }]
        }

        # Deduct purchase amount from user's wallet
        new_balance = wallet - price
        db['customerAccounts'].update_one(
            {'_id': current_user['_id']},
            {'$set': {'walletBalancePeso': new_balance}}
        )

        # Insert owned game and transaction records into database
        db['ownedGameInfo'].insert_one(owned_game)
        db['transactions'].insert_one(transaction)

        return jsonify({
            'success': True,
            'message': 'Purchase successful',
            'newBalance': new_balance
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/refund', methods=['POST'])
def api_refund_game():
    """
    API endpoint to handle game refunds.
    Removes game from user's library, refunds purchase amount to wallet.
    Request JSON: {owned_game_id: <ObjectId>}
    """
    try:
        # Verify user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Not authenticated'}), 401

        data = request.get_json()
        owned_game_id = data.get('owned_game_id')

        # Validate owned_game_id is provided and is valid MongoDB ObjectId
        if not owned_game_id or not ObjectId.is_valid(owned_game_id):
            return jsonify({'error': 'Invalid owned game ID'}), 400

        # Verify owned game exists and belongs to current user
        owned_game = db['ownedGameInfo'].find_one({
            '_id': ObjectId(owned_game_id),
            'ownerUsername': current_user['username']
        })

        if not owned_game:
            return jsonify({'error': 'Game not found in your library'}), 404

        # Look up original game to get refund amount
        game = db['storeGameInfo'].find_one({'gameTitle': owned_game['gameTitle']})
        refund_amount = game.get('currentPricePeso', 0) if game else 0

        # Remove owned game from user's library
        db['ownedGameInfo'].delete_one({'_id': ObjectId(owned_game_id)})

        # Create refund transaction record for audit trail
        refund_transaction = {
            'customerUsername': current_user['username'],
            'customer_id': str(current_user['_id']),
            'refundedGameTitle': owned_game['gameTitle'],
            'refundedGameStore_id': owned_game.get('game_id'),
            'refundedGameLibrary_id': str(owned_game['_id']),
            'transactionDate': datetime.now(),
            'isRefund': True,
            'balanceRefunded': refund_amount
        }

        # Add refunded amount back to user's wallet
        new_balance = current_user.get('walletBalancePeso', 0) + refund_amount
        db['customerAccounts'].update_one(
            {'_id': current_user['_id']},
            {'$set': {'walletBalancePeso': new_balance}}
        )

        # Insert refund transaction record
        db['transactions'].insert_one(refund_transaction)

        return jsonify({
            'success': True,
            'message': 'Refund processed successfully',
            'refundAmount': refund_amount,
            'newBalance': new_balance
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/add-funds', methods=['POST'])
def api_add_funds():
    """
    API endpoint to add funds to user's wallet.
    Validates amount and creates transaction record.
    Request JSON: {amount: <float>}
    """
    try:
        # Verify user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Not authenticated'}), 401

        data = request.get_json()
        amount = data.get('amount')

        # Validate amount is provided and is positive
        if not amount or amount <= 0:
            return jsonify({'error': 'Invalid amount'}), 400

        # Enforce minimum fund amount
        if amount < 10:
            return jsonify({'error': 'Minimum amount is ₱10'}), 400

        # Add funds to user's wallet
        new_balance = current_user.get('walletBalancePeso', 0) + amount
        db['customerAccounts'].update_one(
            {'_id': current_user['_id']},
            {'$set': {'walletBalancePeso': new_balance}}
        )

        # Create fund transaction record for audit trail
        fund_transaction = {
            'customerUsername': current_user['username'],
            'customer_id': str(current_user['_id']),
            'transactionDate': datetime.now(),
            'isRefund': False,
            'fundsAdded': amount,
            'newBalance': new_balance
        }

        # Insert transaction record
        db['transactions'].insert_one(fund_transaction)

        return jsonify({
            'success': True,
            'message': 'Funds added successfully',
            'new_balance': new_balance
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/wallet', methods=['GET'])
def api_get_wallet():
    """
    API endpoint to retrieve the authenticated user's current wallet balance.
    """
    try:
        # Verify user is authenticated
        current_user = get_current_user()
        if not current_user:
            return jsonify({'error': 'Not authenticated'}), 401

        # Get wallet balance from user document
        balance = current_user.get('walletBalancePeso', 0)

        return jsonify({
            'success': True,
            'balance': balance
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/games/<game_id>/reviews', methods=['GET'])
def api_get_game_reviews(game_id):
    """
    API endpoint to retrieve reviews for a specific game by ID.
    Returns reviews mapped to frontend-expected field names.
    """
    try:
        # Validate that game_id is a valid MongoDB ObjectId format
        if not ObjectId.is_valid(game_id):
            return jsonify({'error': 'Invalid game ID format'}), 400

        # Query specific game to get its title
        game = db['storeGameInfo'].find_one({'_id': ObjectId(game_id)})
        if not game:
            return jsonify({'error': 'Game not found'}), 404

        # Fetch reviews for this game by gameTitle
        reviews = list(db['gameReviews'].find({
            'gameTitle': game.get('gameTitle')
        }).limit(50))

        # Map database fields to frontend-expected field names
        mapped_reviews = []
        for review in reviews:
            mapped_reviews.append({
                'author': review.get('authorUsername', 'Anonymous'),
                'playtime': review.get('userPlaytimeHours', 0),
                'date': review.get('datePosted'),
                'recommended': review.get('isRecommended', False),
                'rating': 10 if review.get('isRecommended', False) else 5,  # No rating field in schema, derive from recommendation
                'content': review.get('reviewDescription', '')
            })

        return jsonify({'reviews': mapped_reviews, 'count': len(mapped_reviews)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ========================= ERROR HANDLERS =========================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Use DEBUG environment variable; defaults to False for security
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, port=8000)
