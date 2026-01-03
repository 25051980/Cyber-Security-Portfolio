const jwt = require("jsonwebtoken");
const JWT_SECRET = process.env.JWT_SECRET || "your_jwt_secret";

function authenticateToken(req, res, next) {
  const authHeader = req.headers["authorization"];
  const token = authHeader && authHeader.split(" ")[1];

  if (!token) {
    return res.status(401).json({
      statusCode: 401,
      success: false,
      message: "Authorization token missing"
    });
  }

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({
        statusCode: 403,
        success: false,
        message: "Invalid or expired token"
      });
    }
    req.user = user;
    next();
  });
}

module.exports = authenticateToken;
