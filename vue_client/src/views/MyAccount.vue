<template>
  <div>My MyAccount</div>
</template>

<script>
import axios from "axios";
export default {
  name: "MyAccount",
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");

      this.$store.commit("removeToken");
      this.$router.push("/");
    },
  },
};
</script>

<style lang="scss" scoped>
</style>