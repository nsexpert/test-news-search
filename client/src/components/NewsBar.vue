<template>
  <v-container>
    <v-row justify="center">
      <v-col>
        <div class="text-h4 text-info">Welcome to News Bar</div>
      </v-col>
    </v-row>
    <v-divider class="my-6" />
    <v-row justify="center">
      <v-col cols="6">
        <v-text-field v-model="keyword" density="compact" variant="solo" placeholder="please type keyword..."
          v-debounce="search"></v-text-field>
      </v-col>
      <v-col cols="2">
        <v-select v-model="language" :items="languages" item-title="lang" item-value="value" return-object
          density="compact" variant="solo"></v-select>
      </v-col>
      <v-col cols="8" v-for="(news, idx) in newsList" :key="idx">
        <news-item :newsData="news" />
      </v-col>
    </v-row>
    <loading-circle v-if="loading" />
    <v-row justify="center">
      <v-col cols="8">
        <v-pagination v-model="page" :length="pages" :total-visible="4" rounded="circle"></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import newsItem from '../components/NewsItem.vue'
import LoadingCircle from '../components/LoadingCircle.vue'
import axios from 'axios'
import { defineComponent, ref } from 'vue';
import debounce from '../helper/debounce';

export default defineComponent({
  name: 'NewsBar',
  directives: {
    debounce
  },
  components: {
    newsItem,
    LoadingCircle
  },
  setup() {
    var page = ref(1);
    var pages = ref(0);
    var keyword = ref('');
    var newsList = ref([]);
    var loading = ref(false);
    var languages = ref([
      {
        lang: 'English',
        value: 'en'
      },
      {
        lang: 'German',
        value: 'de'
      }
    ])
    var language = ref({
      lang: "English",
      value: 'en'
    })

    function search() {
      console.log('called search', keyword.value);
      var path = "http://localhost:5000/search";
      loading.value = true;
      axios.post(path, {
        keyword: keyword.value,
        page: page.value,
        language: language.value
      }).then((res) => {
        console.log('res', res.data);
        if (res.data.status === 'no data') {
          newsList.value = [];
          pages.value = 0;
          page.value = 1;
        } else if (res.data.status === 'ok') {
          newsList.value = [...res.data.articles];
          pages.value = Math.floor(parseInt(res.data.totalResults) / 10) + 1;
          console.log('pages', pages, res.data.totalResults, newsList.value, typeof res.data.totalResults);
        }
      }).catch((error) => {
        console.log('error', error)
      }).finally(() => {
        loading.value = false;
      })
      console.log('test', newsList.value);
    }
    return {
      loading,
      search,
      keyword,
      newsList,
      page,
      pages,
      languages,
      language
    }
  },
  watch: {
    page() {
      if (this.keyword != '') {
        this.search();
      }
    },
    language(newVal, oldVal) {
      if (this.keyword != '' && oldVal.value != newVal.value) {
        this.search();
      }
    }
  }
})
</script>

<style scoped></style>
