CREATE DATABASE IF NOT EXISTS techspace;
USE techspace;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) UNIQUE NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  full_name VARCHAR(150),
  bio TEXT,
  role ENUM('visitor', 'member', 'premium', 'admin') DEFAULT 'member',
  position ENUM('developer', 'designer', 'qa', 'security', 'uiux', 'other') DEFAULT 'developer',
  profile_url TEXT,
  github_link VARCHAR(255),
  linkedin_link VARCHAR(255),
  portfolio_link VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);