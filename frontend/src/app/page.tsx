"use client";
import axios from 'axios';
import { useEffect, useState } from 'react';

async function fetchData(url: string) {
    try {
        const response = await axios.get(url);
        if (response.data === null) {
            throw new Error('API request failed');
        }
        return response.data;
    } catch (error) {
        console.error('Error fetching data from', url, error);
        return null;
    }
}

// Importar librerías necesarias y definir función fetchData

export default function Page() {
    const [answeredUnanswered, setAnsweredUnanswered] = useState<any>({});
    const [highestReputation, setHighestReputation] = useState<any>({});
    const [lowestViews, setLowestViews] = useState<any>({});
    const [oldestNewest, setOldestNewest] = useState<any>({});
    const [aeropuertoMasOcupado, setAeropuertoMasOcupado] = useState<any>({});
    const [aerolineaMasActiva, setAerolineaMasActiva] = useState<any>({});
    const [diaMasOcupado, setDiaMasOcupado] = useState<any>({});
    const [aerolineasMasDeDosVuelos, setAerolineasMasDeDosVuelos] = useState<any>({});

    useEffect(() => {
        //  StackExchange
        async function fetchDataAsync() {
            const data1 = await fetchData('http://localhost:5000/api/answered-unanswered');
            if (data1) {
                setAnsweredUnanswered(data1);
            }

            const data2 = await fetchData('http://localhost:5000/api/highest-reputation');
            if (data2) {
                setHighestReputation({
                    pregunta: data2.title,
                    enlace: data2.link,
                    reputacion: data2.owner.reputation
                });
            }

            const data3 = await fetchData('http://localhost:5000/api/lowest-views');
            if (data3) {
                setLowestViews({
                    pregunta: data3.title,
                    enlace: data3.link,
                    vistas: data3.view_count
                });
            }

            const data4 = await fetchData('http://localhost:5000/api/oldest-newest');
            if (data4) {
                setOldestNewest({
                    preguntaMasAntigua: data4.mas_antigua.title,
                    enlaceMasAntigua: data4.mas_antigua.link,
                    preguntaMasReciente: data4.mas_reciente.title,
                    enlaceMasReciente: data4.mas_reciente.link
                });
            }

            // Vuelos en México
            const data5 = await fetchData('http://localhost:5000/api/aeropuerto-mas-ocupado');
            if (data5) {
                setAeropuertoMasOcupado(data5);
            }

            const data6 = await fetchData('http://localhost:5000/api/aerolinea-mas-activa');
            if (data6) {
                setAerolineaMasActiva(data6);{
                };
            }

            const data7 = await fetchData('http://localhost:5000/api/dia-mas-ocupado');
            if (data7) {
                setDiaMasOcupado(data7);
            }

            const data8 = await fetchData('http://localhost:5000/api/aerolineas-mas-de-dos-vuelos');
            if (data8) {
                setAerolineasMasDeDosVuelos(data8);{
                };
            }
        }

        fetchDataAsync();
    }, []);

    return (
        <div>
            <h1>Datos de StackExchange y Vuelos en México</h1>
            <section>
                <h3>StackExchange</h3>
                <h4>Respondidas y No Respondidas</h4>
                <p>No respondidas: {answeredUnanswered.no_respondidas}</p>
                <p>Respondidas: {answeredUnanswered.respondidas}</p>
                <h4>Mayor Reputación</h4>
                <p><a href={highestReputation.pregunta}>{highestReputation.enlace}</a></p>
                <p>Reputación del autor: {highestReputation.reputacion}</p>
                <h4>Menor Número de Vistas</h4>
                <p><a href={lowestViews.pregunta}>{lowestViews.enlace}</a></p>
                <p>Vistas: {lowestViews.vistas}</p>
                <h4>Más Antigua y Más Reciente</h4>
                <p>Pregunta más antigua: <a href={oldestNewest.enlaceMasAntigua}>{oldestNewest.preguntaMasAntigua}</a></p>
                <p>Pregunta más reciente: <a href={oldestNewest.enlaceMasReciente}>{oldestNewest.preguntaMasReciente}</a></p>
            </section>

            <section>
                <h3>Vuelos en México</h3>
                <section>
                    <h4>Aeropuerto Más Ocupado</h4>
                    <p>{aeropuertoMasOcupado.aeropuerto_mas_ocupado}</p>
                    <p>Movimientos: {aeropuertoMasOcupado.movimientos}</p>
                    <h4>Aerolínea Más Activa</h4>
                    <p>{aerolineaMasActiva.aerolinea_mas_activa}</p>
                    <p>Cantidad de vuelos: {aerolineaMasActiva.cantidad_vuelos}</p>
                </section>
                <section>
                    <h4>Día Más Ocupado</h4>
                    <p>{diaMasOcupado.dia_mas_ocupado}</p>
                    <p>Cantidad de vuelos: {diaMasOcupado.cantidad_vuelos}</p>
                    <h4>Aerolíneas con Más de Dos Vuelos</h4>
                    <ul>
                        {aerolineasMasDeDosVuelos.aerolineas && aerolineasMasDeDosVuelos.aerolineas.map((aerolinea: string, index: number) => (
                            <li key={index}>{aerolinea}</li>
                        ))}
                    </ul>
                </section>
            </section>
        </div>
    );
}
