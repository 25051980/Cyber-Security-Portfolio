const mongoose = require("mongoose");

const ProductSchema = new mongoose.Schema({
  name: String,
  description: String,
  price: Number,
  category: String,
  available: Boolean,
  image: {
    data: Buffer,
    contentType: String,
  },
});

module.exports = mongoose.model("Product", ProductSchema);
