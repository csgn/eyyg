const express = require("express");
const router = express.Router();
const pool = require("./database");

router.get("/methods", async (req, res) => {
  pool.query("SELECT request_method FROM serverLog", (error, results) => {
    if (error) {
      throw error;
    }
    const methods = results.rows.map((row) => row.request_method);
    res.status(200).json(methods);
  });
});

router.get("/endpoints", async (req, res) => {
  pool.query(
    "SELECT DISTINCT request_endpoint FROM serverlog",
    (error, results) => {
      if (error) {
        console.log(error);
        throw error;
      }
      const endpoints = results.rows.map((row) => row.request_endpoint);
      res.status(200).json(endpoints);
    }
  );
});

router.get("/statuses", async (req, res) => {
  pool.query("SELECT request_status FROM serverLog", (error, results) => {
    if (error) {
      throw error;
    }
    const statuses = results.rows.map((row) => row.request_status);
    res.status(200).json(statuses);
  });
});

router.get("/whole-time", async (req, res) => {
  pool.query(
    `SELECT request_endpoint, request_status, request_time::TIMESTAMP::DATE, count(*) FROM serverLog 
    WHERE request_endpoint = '${req.query.url}' and request_method = '${req.query.method}'
    GROUP BY request_endpoint, request_status, request_time::TIMESTAMP::DATE ORDER BY 3`,
    (error, results) => {
      if (error) {
        throw error;
      }
      const data = results.rows.map((row) => row.request_time);
      res.status(200).json(results.rows);
    }
  );
});

module.exports = router;
