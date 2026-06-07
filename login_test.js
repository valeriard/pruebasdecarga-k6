import http from 'k6/http';
import { check } from 'k6';
import { SharedArray } from 'k6/data';
import papaparse from 'https://jslib.k6.io/papaparse/5.1.1/index.js';

const usuarios = new SharedArray('usuarios', function () {
  return papaparse.parse(open('./users.csv'), {
    header: true,        
    skipEmptyLines: true, 
  }).data;
});


export const options = {
  scenarios: {
    carga_login: {
      executor: 'constant-arrival-rate', 
      rate: 20,             
      timeUnit: '1s',       
      duration: '1m',       
      preAllocatedVUs: 50,  
      maxVUs: 100,          
    },
  },

  // 3) Las reglas que debe cumplir la prueba para considerarse "aprobada"
  thresholds: {
    http_req_duration: ['p(95)<1500'], 
    http_req_failed: ['rate<0.03'], 
    http_reqs: ['rate>=20'],   
  },
};


export default function () {
  
  const u = usuarios[Math.floor(Math.random() * usuarios.length)];

  const url = 'https://fakestoreapi.com/auth/login';

  const cuerpo = JSON.stringify({
    username: u.user,    
    password: u.passwd,  
  });

  const parametros = {
    headers: { 'Content-Type': 'application/json' },
  };

  
  const res = http.post(url, cuerpo, parametros);

 
  check(res, {
    'el status es 200': (r) => r.status === 200,
    'respondio en menos de 1,5s': (r) => r.timings.duration < 1500,
    'devolvio un token': (r) => r.body && String(r.body).includes('token'),
  });
}
