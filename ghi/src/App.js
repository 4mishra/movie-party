import './App.css';
import TestHome from './components/TestHome';
import MovieCardList from './components/cards/MovieCardList';
import {
  Route,
  BrowserRouter,
  Routes
} from "react-router-dom";
import Nav from './Nav';

function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div>
        <Routes>
          <Route index element={<MovieCardList />} />
          <Route path="testhome" element={<TestHome />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App;
