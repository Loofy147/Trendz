import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

const getProducts = () => {
  return axios.get(API_URL + 'products/');
};

const getProduct = (id) => {
  return axios.get(API_URL + `products/${id}/`);
};

const productService = {
  getProducts,
  getProduct,
};

export default productService;
