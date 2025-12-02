<template>
  <div>
    <h2>Products</h2>
    <ul>
      <li v-for="p in products" :key="p.id">
        {{ p.name }} — {{ p.price.toFixed(2) }} 
        <button @click="sell(p.id)">Sell 1</button>
      </li>
    </ul>

    <h3>Add product</h3>
    <input v-model="name" placeholder="name" />
    <input v-model.number="price" placeholder="price" type="number" />
    <button @click="addProduct">Add</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return { products: [], name: '', price: 0 }
  },
  mounted() { this.fetch() },
  methods: {
    async fetch() {
      const res = await axios.get('/api/products')
      this.products = res.data
    },
    async addProduct() {
      await axios.post('/api/products', { name: this.name, price: this.price })
      this.name = ''; this.price = 0
      this.fetch()
    },
    async sell(productId) {
      await axios.post('/api/sales', { product_id: productId, quantity: 1 })
      alert('Sale recorded')
    }
  }
}
</script>
