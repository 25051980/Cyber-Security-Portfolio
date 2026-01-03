const express = require("express");
const jwt = require("jsonwebtoken");

const router = express.Router();
const JWT_SECRET = process.env.JWT_SECRET || "your_jwt_secret";


const demoUser = { email: "admin", password: "admin123" };

// LOGIN route
router.post("/login", (req, res) => {
  const { email, password } = req.body;

  // Validate request body
  if (!email || !password) {
    return res.status(400).json({
      statusCode: 400,
      success: false,
      message: "Email and password are required."
    });
  }

  // Simple credential check
  if (email === demoUser.email && password === demoUser.password) {
    const token = jwt.sign({ email }, JWT_SECRET, { expiresIn: "1h" });
    return res.status(200).json({
      statusCode: 200,
      success: true,
      message: "Login successful.",
      token
    });
  }

  // Invalid credentials
  return res.status(401).json({
    statusCode: 401,
    success: false,
    message: "Invalid email or password."
  });
});

module.exports = router;
