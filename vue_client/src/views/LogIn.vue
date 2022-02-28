<template>
  <div class="w-1/3 mx-auto mt-12 shadow-md pt-2">
    <h1 class="text-center text-gray-900 text-4xl mb-2">Log In</h1>
    <form
      class="bg-white rounded px-8 pt-6 pb-8 mb-4"
      @submit.prevent="submitForm()"
    >
      <div class="mb-4">
        <label
          class="block text-gray-700 text-sm font-bold mb-2"
          for="username"
        >
          Username
        </label>
        <input
          class="
            shadow
            appearance-none
            border
            rounded
            w-full
            py-2
            px-3
            text-gray-700
            leading-tight
            focus:outline-none focus:shadow-outline
          "
          v-model="username"
          type="text"
          placeholder="Username"
        />
      </div>
      <div class="mb-4">
        <label
          class="block text-gray-700 text-sm font-bold mb-2"
          for="password"
        >
          Password
        </label>
        <input
          class="
            shadow
            appearance-none
            border
            rounded
            w-full
            py-2
            px-3
            text-gray-700
            leading-tight
            focus:outline-none focus:shadow-outline
          "
          v-model="password"
          type="password"
          placeholder="Password"
        />
      </div>

      <div class="errors" v-if="errors.length">
        <p
          v-for="error in errors"
          :key="error"
          class="text-red-400 italic mb-2"
        >
          {{ error }}
        </p>
      </div>

      <div class="flex items-center justify-between">
        <a
          class="
            inline-block
            align-baseline
            font-bold
            text-sm text-blue-500
            hover:text-blue-800
          "
          href="#"
        >
          Forgot Password?
        </a>
        <button
          class="
            bg-blue-500
            hover:bg-blue-700
            text-white
            font-bold
            py-2
            px-4
            rounded
            focus:outline-none focus:shadow-outline
          "
          type="submit"
        >
          Log in
        </button>
      </div>
      <hr class="my-2" />
      <p class="text">
        Or
        <router-link to="/sign-up" class="text-sky-500 mx-4"
          >click here
        </router-link>
        to sign up
      </p>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "LogIn",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
      errors: [],
    };
  },

  mounted() {
    document.title = "Log in | Djackets";
  },

  methods: {
    submitForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");

      this.errors = [];

      if (this.username === "") {
        this.errors.push("Please enter your user name!");
      }

      if (this.password === "") {
        this.errors.push("Please enter password !");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };

        axios
          .post(`/api/v1/token/login/`, formData)
          .then((response) => {
            const token = response.data.auth_token;

            this.$store.commit("setToken", token);

            axios.defaults.headers.common["Authorization"] = "Token " + token;

            localStorage.setItem("token", token);

            const pathTo = this.$route.query.to || "/cart";

            this.$router.push(pathTo);
          })
          .catch((err) => {
            console.log(err);
            if (err.response) {
              for (const property in err.response.data) {
                this.errors.push(
                  `${property} : ${err.response.data[property]}`
                );
              }
              console.log(JSON.stringify(err.response.data));
            } else if (err.message) {
              this.errors.push("Something went wrong, please try again later");
              console.log(JSON.stringify(err));
            }
          });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
</style>