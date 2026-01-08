const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();
const PORT = 8000;

app.use(cors());
app.use(express.json());

//MongoDB connection
mongoose.connect('mongodb://database:27017/hackstack', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => console.log('MongoDB connected'))
  .catch(err => console.log('MongoDB connection error:', err));

//Item schema
const ItemSchema = new mongoose.Schema({
  name: { type: String, required: true }
});

const Item = mongoose.model('Item', ItemSchema);

//Routes
app.get('/api/health', (req, res) => {
  res.json({ message: 'Backend is running!' });
});

app.get('/api/items', async (req, res) => {
  const items = await Item.find();
  res.json(items);
});

app.post('/api/items', async (req, res) => {
  const { name } = req.body;
  const item = new Item({ name });
  await item.save();
  res.json(item);
});

app.delete('/api/items/:id', async (req, res) => {
  await Item.findByIdAndDelete(req.params.id);
  res.json({ message: 'Item deleted' });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
