const Pool = require("pg").Pool;

let POSTGRES_USER = process.env.POSTGRES_USER;
let POSTGRES_HOST = process.env.POSTGRES_HOST;
let POSTGRES_PASSWORD = process.env.POSTGRES_PASSWORD;
let POSTGRES_NAME = process.env.POSTGRES_NAME;

const pool = new Pool({
  user: POSTGRES_USER,
  host: POSTGRES_HOST,
  database: POSTGRES_NAME,
  password: POSTGRES_PASSWORD,
  port: 5432,
});

module.exports = pool;
