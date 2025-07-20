import { render, screen } from '@testing-library/react';
import HomePage from './HomePage';

test('renders home page', () => {
  render(<HomePage />);
  const linkElement = screen.getByText(/Home Page/i);
  expect(linkElement).toBeInTheDocument();
});
