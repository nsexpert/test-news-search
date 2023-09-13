<template>
  <div>
    <news-bar/>
  </div>
</template>

<script>
import NewsBar from './components/NewsBar.vue';
export default {
  name: 'App',
  components: {
    NewsBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
