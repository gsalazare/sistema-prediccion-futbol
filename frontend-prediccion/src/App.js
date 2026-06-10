import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [ids, setIds] = useState({ idLocal: '', idVisita: '' });
  const [resultado, setResultado] = useState(null);

  const analizar = async () => {
    try {
      // Conexión a tu backend Java en puerto 8080
      const res = await axios.post('http://localhost:8080/api/partidos/analizar', ids);
      setResultado(res.data);
    } catch (error) {
      alert("Error al conectar con Java. Asegúrate de que Spring Boot esté corriendo.");
    }
  };

  return (
    <div style={{ padding: '50px', fontFamily: 'Arial' }}>
      <h1>Analizador Deportivo IA</h1>
      <input placeholder="ID Local" onChange={(e) => setIds({...ids, idLocal: e.target.value})} />
      <input placeholder="ID Visita" onChange={(e) => setIds({...ids, idVisita: e.target.value})} />
      <button onClick={analizar}>Analizar Partido</button>

      {resultado && (
        <div style={{ marginTop: '20px', border: '1px solid #ccc', padding: '10px' }}>
          <h2>Resultado: {resultado.prediccionGanador}</h2>
          <p>Proyección de Goles: {resultado.prediccionGoles}</p>
        </div>
      )}
    </div>
  );
}

export default App;