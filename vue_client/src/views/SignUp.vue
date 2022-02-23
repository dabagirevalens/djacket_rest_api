<template>
  <div class="w-1/3 mx-auto mt-12 shadow-md pt-2">
    <h1 class="text-center text-gray-900 text-4xl mb-2">Sign Up</h1>
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
        <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
          Email
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
          v-model="email"
          type="text"
          placeholder="Email"
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
      <div class="mb-4">
        <label
          class="block text-gray-700 text-sm font-bold mb-2"
          for="confirm-password"
        >
          Confirm Password
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
          v-model="confirmPassword"
          type="password"
          placeholder="Confirm Password"
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
          Sign Up
        </button>
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
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
      errors: [],
    };
  },

  methods: {
    submitForm() {
      this.errors = [];

      if (this.username === "") {
        this.errors.push("Please enter your user name!");
      }

      if (this.email === "") {
        this.errors.push("Please enter your email !");
      }

      if (this.password === "") {
        this.errors.push("Please enter password !");
      }

      if (this.password !== this.confirmPassword) {
        this.errors.push("Password don't match !");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          email: this.email,
          password: this.password,
        };

        axios.post(`/api/v1/users/`, formData).then(() => {
          this.$route.push("/log-in");
        }).catch(err =>{
            if(err.response){
                for (const property in err.response.data){
                    this.errors.push (`${property} : ${err.response.data[property]}`)
                }
                console.log(JSON.stringify(err.response.data))
            }else if(err.message){
                this.errors.push('Something went wrong, please try again later')
                console.log(JSON.stringify(err))  
            }
        });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
</style>