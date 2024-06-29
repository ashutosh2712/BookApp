import { RouterProvider, createBrowserRouter } from "react-router-dom";
import "./App.css";
import Layout from "./components/Layout";
import Book from "./pages/Book";
import Books from "./pages/Books";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Books />,
      },
      {
        path: "books/:id",
        element: <Book />,
      },
    ],
  },
]);
function App() {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
