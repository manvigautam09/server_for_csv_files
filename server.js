const express = require("express");
const fs = require("fs");
const path = require("path");
const cors = require("cors");

const app = express();
const PORT = 3005;

// enabling CORS for any unknown origin
app.use(cors());

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, "public")));

// Define a route to serve CSV files
app.get("/csv/:filename", (req, res) => {
  const filename = req.params.filename;
  const filePath = path.join(__dirname, "public", filename + ".csv");

  // Check if the file exists
  if (fs.existsSync(filePath)) {
    res.setHeader("Content-Type", "text/csv");
    const fileStream = fs.createReadStream(filePath);
    fileStream.pipe(res);
  } else {
    res.status(404).send("File not found");
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
