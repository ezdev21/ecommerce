import express from 'express';

const app = express();
const PORT = process.env.PORT || 4000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.send('The Ecommerce Project');
})

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});