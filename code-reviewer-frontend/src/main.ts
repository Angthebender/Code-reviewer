import { createApp } from "vue";
import App from "./App.vue";
import { Quasar } from "quasar";
import "quasar/dist/quasar.css";

const app = createApp(App);
app.use(Quasar);
app.mount("#app");
