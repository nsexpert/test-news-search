<template>
  <v-card class="w-100 pa-3" :elevation="8">
    <v-row>
      <v-col cols="3">
        <v-img
          :src="newsData.urlToImage == null ? './default.png': newsData.urlToImage"
          class="h-100 w-100"
          :alt="'image'"
        />
      </v-col>
      <v-col cols="9 text-left font-weight-light text-grey">
        <div class="text-green">{{ newsData.title }} </div>
        <v-divider/>
        <div> Where to find: <a :href="newsData.url">Read the article</a></div>
        <v-divider/>
        <div> Published at: {{(new Date(newsData.publishedAt)).toDateString()}} </div>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'newsItem',
  props: {
    newsData: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const news = ref(props.newsData);
    return {
      news
    };
  },
})
</script>

<style scoped></style>
