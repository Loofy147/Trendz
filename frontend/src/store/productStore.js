import { create } from 'zustand';
import productService from '../services/productService';

const useProductStore = create((set, get) => ({
  products: [],
  filteredProducts: [],
  loading: false,
  error: null,
  filters: {
    priceRange: [0, 10000],
    source: 'all',
    sortBy: 'trend_score',
  },

  fetchProducts: async () => {
    set({ loading: true });
    try {
      const response = await productService.getProducts();
      set({
        products: response.data,
        filteredProducts: response.data,
        loading: false,
      });
    } catch (error) {
      set({ error: 'Failed to fetch products', loading: false });
    }
  },

  setFilters: (newFilters) => {
    const filters = { ...get().filters, ...newFilters };
    const filteredProducts = get().products.filter((product) => {
      // Apply filtering logic
      return (
        product.price >= filters.priceRange[0] &&
        product.price <= filters.priceRange[1]
      );
    });
    set({ filters, filteredProducts });
  },
}));

export default useProductStore;
