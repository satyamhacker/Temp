const mongoose = require('mongoose');

// Define the signup schema
const signupSchema = new mongoose.Schema({
 
  email: {
    type: String,
    required: true,
    unique: true,
    trim: true,
  },
  password: {
    type: String,
    required: true,
  }
});

// Create the Signup model
const SignupData = mongoose.model('SignupData', signupSchema);

module.exports = SignupData;
