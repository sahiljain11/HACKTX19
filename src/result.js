import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css';
import Result from './Components/ResultPage';
import * as serviceWorker from './Components/serviceWorker';

// console.log("result is loaded")
ReactDOM.render(<Result />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
