import "./App.css";
import { useEffect, useState } from "react";
import { Row } from "react-bootstrap";
function App() {
  document.title = `Currency Convert`;
  const [amount, setAmount] = useState();
  const [ConvertedAmount, setConvertedAmount] = useState();
  const [fromCurrencr, setFromCurrencr] = useState();
  const [toCurrency, setToCurrency] = useState();
  const [items, setItem] = useState([]);

  var myHeaders = new Headers();
  myHeaders.append("apikey", "aQUIcH9eAvJa4llHuCYrLKWCDB08rUam");

  var requestOptions = {
    method: "GET",
    redirect: "follow",
    headers: myHeaders,
  };

  useEffect(() => {
    fetch("https://api.apilayer.com/fixer/symbols", requestOptions)
      .then((response) => response.json())
      .then((result) => setItem(result.symbols))
      .catch((error) => console.log("error", error));
  }, []);

  useEffect(() => {
    fetch(
      `https://api.apilayer.com/fixer/convert?to=${toCurrency}&from=${fromCurrencr}&amount=${amount}`,
      requestOptions
    )
      .then((response) => response.json())
      .then((result) => setConvertedAmount(result.result.toFixed(2)))
      .catch((error) => console.log("error", error));
  }, [amount, fromCurrencr, toCurrency]);

  return (
    <div className="group">
      <div className="input">
        <input onChange={(e) => setAmount(e.target.value)}></input>
        <select onChange={(e) => setFromCurrencr(e.target.value)}>
          {Object.keys(items).map((currency) => (
            <option value={currency}>{items[currency]}</option>
          ))}
        </select>
      </div>
      <div className="input">
        <input value={ConvertedAmount}></input>
        <select onChange={(ev) => setToCurrency(ev.target.value)}>
          {Object.keys(items).map((currency) => (
            <option value={currency}>{items[currency]}</option>
          ))}
        </select>
      </div>
      <p className="Result1">
        <span>{amount}</span>
        <span> {items[fromCurrencr]} equals</span>
      </p>
      <p className="Result2">
        <span>
          {ConvertedAmount} {items[toCurrency]}
        </span>
      </p>
    </div>
  );
}

export default App;
