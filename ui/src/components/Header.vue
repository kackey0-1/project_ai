<template>
<v-app-bar
  app
  color="primary"
  dark
>
  <div class="d-flex align-center">
    <v-img
      alt="Vuetify Logo"
      class="shrink mr-2"
      contain
      src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
      transition="scale-transition"
      width="40"
    />
  </div>

  <v-spacer></v-spacer>

  <v-btn icon>
    <router-link to="/"><v-icon color="white">mdi-home</v-icon></router-link>
  </v-btn>
  <v-btn icon>
    <router-link to="/about"><v-icon color="white">mdi-read</v-icon></router-link>
  </v-btn>
  <v-btn icon>
    <router-link to="/ai"><v-icon color="white">mdi-human-greeting</v-icon></router-link>
  </v-btn>
</v-app-bar>
</template>
