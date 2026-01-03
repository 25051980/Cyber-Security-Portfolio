const express = require("express");
const fs = require("fs");
const path = require("path");
const Product = require("../models/Product");
const authenticateToken = require("../middleware/auth");

const router = express.Router();
const uploadDir = path.join(__dirname, "..", "data", "images");

// CREATE product
router.post("/", authenticateToken, async (req, res) => {
  const { name, description, price, category, available, image } = req.body;

  if (!name || !price || !category || !image) {
    return res.status(400).json({ error: "Missing required fields" });
  }


  try {
    const extMatch = image.match(/^data:(image\/\w+);base64,/);
    if (!extMatch) return res.status(400).json({ error: "Invalid image format" });

    const contentType = extMatch[1];
    const base64Data = image.replace(/^data:image\/\w+;base64,/, "");
    const imgBuffer = Buffer.from(base64Data, "base64");

    const product = new Product({
      name,
      description,
      price,
      category,
      available,
      image: { data: imgBuffer, contentType },
    });

    await product.save();
    const productResponse = product.toObject();
    delete productResponse.image;

    res.status(201).json(productResponse);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Internal server error" });
  }
});

// READ products
router.get("/", async (req, res) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch {
    res.status(500).json({ error: "Failed to fetch products" });
  }
});

// UPDATE product
router.put("/:id", authenticateToken, async (req, res) => {
  const { id } = req.params;
  const { name, description, price, category, available, image } = req.body;

  try {
    const product = await Product.findById(id);
    if (!product) return res.status(404).json({ error: "Product not found" });

    if (image) {
      const extMatch = image.match(/^data:(image\/\w+);base64,/);
      if (!extMatch) return res.status(400).json({ error: "Invalid image format" });

      const contentType = extMatch[1];
      const base64Data = image.replace(/^data:image\/\w+;base64,/, "");
      const imgBuffer = Buffer.from(base64Data, "base64");

      product.image = {
        data: imgBuffer,
        contentType,
      };
    }

    // Update other fields
    product.name = name;
    product.description = description;
    product.price = price;
    product.category = category;
    product.available = available;

    await product.save();

    // Return updated product but exclude image data from response (optional)
    const productResponse = product.toObject();
    delete productResponse.image;

    res.json(productResponse);
    console.log("UPDATED");
  } catch (err) {
    console.log("ERROR", err);
    res.status(500).json({ error: "Internal server error" });
  }
});


// DELETE product
router.delete("/:id", authenticateToken, async (req, res) => {
  console.log("teste")
  try {
    console.log("ID", req.params.id)
    const product = await Product.findById(req.params.id);
    if (!product) return res.status(404).json({ error: "Product not found" });

    await product.deleteOne();
    res.json({ success: true });
  } catch {
    res.status(500).json({ error: "Internal server error" });
  }
});

module.exports = router;
