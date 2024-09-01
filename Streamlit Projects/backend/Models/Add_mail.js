const mongoose = require('mongoose');

// Define the AddMail schema
const AddMailSchema = new mongoose.Schema({
  subject: {
    type: String,
    required: true,
    trim: true,
  },
  content: {
    type: String,
    required: true,
    trim: true,
  },
  senderEmail: {
    type: String,
    required: true,
    trim: true,
  },
  receiverEmail: {
    type: String,
    required: true,
    trim: true,
  },
  timeStamp: {
    type: String, // Assuming you want to store the timestamp as a string
    required: true,
    trim: true,
  },
  emailRead: {
    type: Boolean, // Change the type to Boolean
    default: false, // Set the default value to false if you want it to default to unread
    trim: true,
  },
  // You can include other fields relevant to user AddMail here
});

// Create the AddMail model
const AddMail = mongoose.model('mailsData', AddMailSchema);

module.exports = AddMail;
