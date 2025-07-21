import React from 'react';

const Product = ({ product }) => {
  return (
    <li>
      {product.name} - ${product.current_price}
    </li>
  );
};

export default Product;
