import json
import argparse
from datetime import datetime


def format_value(v):
    if isinstance(v, float):
        return f"{v:.2f}"
    return str(v)


def metrics_to_table(metrics):
    rows = []
    for name, meta in metrics.items():
        mtype = meta.get('type', '')
        values = meta.get('values', {}) if isinstance(meta, dict) else {}
        if values:
            for k, v in values.items():
                rows.append((name, mtype, k, format_value(v)))
        else:
            # fallback: flatten other keys
            for k, v in (meta.items() if isinstance(meta, dict) else []):
                if k == 'type':
                    continue
                rows.append((name, mtype, k, format_value(v)))
    return rows


def generate_html(data, title="Reporte k6"):
    metrics = data.get('metrics', {})
    rows = metrics_to_table(metrics)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    html = []
    html.append(f"<html><head><meta charset=\"utf-8\"><title>{title}</title>")
    html.append("<style>body{font-family:Arial,Helvetica,sans-serif;margin:20px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:8px}th{background:#f4f4f4;text-align:left}</style>")
    html.append("</head><body>")
    html.append(f"<h1>{title}</h1>")
    html.append(f"<p>Generado: {now}</p>")

    if rows:
        html.append("<table>")
        html.append("<thead><tr><th>Métrica</th><th>Tipo</th><th>Estadística</th><th>Valor</th></tr></thead>")
        html.append("<tbody>")
        for name, mtype, stat, val in rows:
            html.append(f"<tr><td>{name}</td><td>{mtype}</td><td>{stat}</td><td>{val}</td></tr>")
        html.append("</tbody></table>")
    else:
        html.append("<p>No se encontraron métricas en el JSON proporcionado.</p>")

    # Optional: include summary if present
    summary = data.get('root_group') or data.get('summary')
    if summary:
        html.append("<h2>Resumen</h2>")
        html.append(f"<pre>{json.dumps(summary, indent=2)}</pre>")

    html.append("</body></html>")
    return '\n'.join(html)


def main():
    parser = argparse.ArgumentParser(description='Convertir JSON de k6 a HTML simple')
    parser.add_argument('input', help='Archivo JSON de entrada (ej. results.json)')
    parser.add_argument('output', nargs='?', default='report.html', help='Archivo HTML de salida (por defecto: report.html)')
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as f:
        data = json.load(f)

    html = generate_html(data, title='Reporte de ejecución k6')

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Reporte generado: {args.output}")


if __name__ == '__main__':
    main()
