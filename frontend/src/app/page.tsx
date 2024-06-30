// page.tsx

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Page() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/data');
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Frontend de la Prueba Técnica</h1>
      {data ? (
        <div>
          <h2>Datos del Backend:</h2>
          <pre>{JSON.stringify(data, null, 2)}</pre>
          {/* Aquí puedes renderizar gráficos y otros componentes según los datos recibidos */}
        </div>
      ) : (
        <p>Cargando datos...</p>
      )}
    </div>
  );
}

export default Page;
