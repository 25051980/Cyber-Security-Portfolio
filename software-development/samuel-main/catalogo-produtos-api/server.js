require("dotenv").config();
const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const connectDB = require("./config/db");

const app = express();
const PORT = process.env.PORT || 5001;

connectDB();

// Middleware
app.use(cors({ origin: "http://localhost:3000" }));
app.use(express.json({ limit: "10mb" }));

// Health Check
app.get("/api/health", async (req, res) => {
  try {
    const dbState = mongoose.connection.readyState;
    const states = ["disconnected", "connected", "connecting", "disconnecting"];

    return res.status(200).json({
      statusCode: 200,
      success: true,
      message: "API is running 🚀",
      database: states[dbState]
    });
  } catch (error) {
    return res.status(500).json({
      statusCode: 500,
      success: false,
      message: "API is running but DB check failed ❌",
      error: error.message
    });
  }
});

// Routes
app.use("/api/products", require("./routes/productRoutes"));
app.use("/api/auth", require("./routes/authRoutes"));

// 404 Handler
app.use((req, res) => {
  res.status(404).json({
    statusCode: 404,
    success: false,
    message: "Resource not found"
  });
});

// Global Error Handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.statusCode || 500).json({
    statusCode: err.statusCode || 500,
    success: false,
    message: err.message || "Internal Server Error"
  });
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
