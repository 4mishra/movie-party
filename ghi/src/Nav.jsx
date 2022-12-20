import {NavLink} from "react-router-dom"

function Nav() {
  return (
    <nav>
      <div>
        <ul>
          <li>
            <NavLink aria-current="page" to="/">Home</NavLink>
          </li>
          <li>
            <NavLink aria-current="page" to="/testhome">Test Home</NavLink>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Nav;
