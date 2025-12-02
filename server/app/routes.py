from flask import Blueprint, jsonify, request
from app.models import UserModel
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)

@main.route('/users', methods=['POST'])
def create_user():
    data = request.json
    
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Username, Email, dan Password wajib diisi!'}), 400

    try:
        hashed_pw = generate_password_hash(data['password'], method='pbkdf2:sha256')
        
        user_data = {
            'username': data['username'],
            'email': data['email'],
            'password_hash': hashed_pw,
            'full_name': data.get('full_name'),
            'bio': data.get('bio'),
            'role': data.get('role', 'member'),
            'position': data.get('position', 'developer'),
            'profile_url': data.get('profile_url'),
            'github_link': data.get('github_link'),
            'linkedin_link': data.get('linkedin_link'),
            'portfolio_link': data.get('portfolio_link')
        }
        new_id = UserModel.create(user_data)
        
        return jsonify({
            'message': 'User Techspace berhasil dibuat', 
            'id': new_id,
            'username': user_data['username']
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/users', methods=['GET'])
def get_users():
    try:
        users = UserModel.get_all()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    user = UserModel.get_by_id(user_id)
    if not user:
        return jsonify({'message': 'User tidak ditemukan'}), 404
    return jsonify(user), 200

@main.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    
    current_user = UserModel.get_by_id(user_id)
    if not current_user:
        return jsonify({'message': 'User tidak ditemukan'}), 404
    
    try:
        updated_data = {
            'username': data.get('username', current_user['username']),
            'email': data.get('email', current_user['email']),
            'full_name': data.get('full_name', current_user['full_name']),
            'bio': data.get('bio', current_user['bio']),
            'role': data.get('role', current_user['role']),
            'position': data.get('position', current_user['position']),
            'profile_url': data.get('profile_url', current_user['profile_url']),
            'github_link': data.get('github_link', current_user['github_link']),
            'linkedin_link': data.get('linkedin_link', current_user['linkedin_link']),
            'portfolio_link': data.get('portfolio_link', current_user['portfolio_link'])
        }
        UserModel.update(user_id, updated_data)
        
        return jsonify({'message': 'Data user berhasil diupdate', 'data': updated_data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    affected = UserModel.delete(user_id)
    
    if affected == 0:
        return jsonify({'message': 'User tidak ditemukan'}), 404
        
    return jsonify({'message': 'User berhasil dihapus'}), 200