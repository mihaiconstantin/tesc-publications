'use strict';

const jQuery = require('jquery');
global.jQuery = jQuery;

const Tether = require('Tether');
global.Tether = Tether;

const Bootstrap = require('Bootstrap');
import 'bootstrap/dist/css/bootstrap.min.css';

import Vue from 'vue'
import App from './App.vue'

// Import and register componenets here.



new Vue({
  el: '#app',
  render: h => h(App)
})
