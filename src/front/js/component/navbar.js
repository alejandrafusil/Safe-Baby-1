import React from "react";
import { Link } from "react-router-dom";
import "../../styles/navbar.css";
import LogoBebe from "../../img/logo-nuevo-safe baby.png";
export const Navbar = () => {
	return (
		<nav className="navbar navbar py-3">
			<Link to="/Home">
				<img className="navbar-brand" src={LogoBebe} />
			</Link>
			<div className="container-buttons gap-4 d-flex justify-content-end">
				<div className="">
					<Link to="/Home">
						<button className="btn btn-navbar text">Inicio</button>
					</Link>
				</div>
				<div className="">
					<Link to="/Progress">
						<button className="btn btn-navbar">Progreso</button>
					</Link>
				</div>
				<div className="">
					<Link to="/Foro">
						<button className="btn btn-navbar">Chat</button>
					</Link>
				</div>
				<div className="">
					<Link to="/Citas">
						<button className="btn btn-navbar">Citas</button>
					</Link>
				</div>
				<div className="">
					<Link to="/Perfil">
						<button className="btn btn-navbar">Perfil</button>
					</Link>
				</div>
				<div className="">
					<Link to="/">
						<button className="btn btn-navbar">Logout</button>
					</Link>
				</div>
			</div>
		</nav>
	);
};
