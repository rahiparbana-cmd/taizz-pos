<template>
  <div id="app" class="container">
    <h1>Taizz POS (Demo)</h1>
    <ProductList />
  </div>
</template>

<script>
import ProductList from './components/ProductList.vue'
export default {
  components: { ProductList }
}
</script>

<style>
.container { max-width: 900px; margin: 2rem auto; font-family: Arial, Helvetica, sans-serif; }
</style>
