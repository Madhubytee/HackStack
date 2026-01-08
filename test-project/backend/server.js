const express = require('express');
const cors = require('cors');
const { Pool } = require('pg');

const app = express();
const PORT = 8000;

app.use(cors());
app.use(express.json());

//Database connection
const pool = new Pool({
  host: 'database',
  port: 5432,
  user: 'postgres',
  password: 'postgres',
  database: 'hackstack'
});

//Initializes the database
pool.query(`
  CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
  )
`).then(() => console.log('Database initialized'));

//Routes
app.get('/api/health', (req, res) => {
  res.json({ message: 'Backend is running!' });
});

app.get('/api/items', async (req, res) => {
  const result = await pool.query('SELECT * FROM items');
  res.json(result.rows);
});

app.post('/api/items', async (req, res) => {
  const { name } = req.body;
  const result = await pool.query(
    'INSERT INTO items (name) VALUES ($1) RETURNING *',
    [name]
  );
  res.json(result.rows[0]);
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
