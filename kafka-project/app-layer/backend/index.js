const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
require("dotenv").config();

const app = express();
app.use(cors());
app.use(bodyParser.json());

const endpoints = require("./endpoints");

app.use("/api", endpoints);

app.get("/", (req, res) => {
  res.send("Kafka Project API");
});

let PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});
