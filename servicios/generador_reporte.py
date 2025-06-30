from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import datetime

def generar_pdf(respuestas, diagnostico_clave, diagnosticos):
    # Crear el PDF en memoria
    from io import BytesIO
    buffer = BytesIO()
    
    # Configurar documento
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    # Estilos
    estilos = getSampleStyleSheet()
    estilos.add(ParagraphStyle(
        name='Titulo',
        fontSize=16,
        alignment=1,
        spaceAfter=20,
        textColor=colors.darkblue
    ))
    estilos.add(ParagraphStyle(
        name='Subtitulo',
        fontSize=14,
        spaceAfter=10,
        textColor=colors.darkblue
    ))
    estilos.add(ParagraphStyle(
        name='NormalCentrado',
        alignment=1,
        spaceAfter=10
    ))
    
    elementos = []
    
    # Título
    elementos.append(Paragraph("INFORME DE EVALUACIÓN DE ESTRÉS LABORAL", estilos['Titulo']))
    elementos.append(Paragraph(f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y')}", estilos['NormalCentrado']))
    elementos.append(Spacer(1, 30))
    
    # Sección de diagnóstico
    diag = diagnosticos.get(diagnostico_clave, diagnosticos.get("CA", {}))
    elementos.append(Paragraph("DIAGNÓSTICO", estilos['Subtitulo']))
    elementos.append(Paragraph(diag.get('DIAGNOSTICO', 'Sin diagnóstico'), estilos['Heading2']))
    elementos.append(Spacer(1, 15))
    
    # Detalles del diagnóstico
    elementos.append(Paragraph(f"<b>Nivel de riesgo:</b> {diag.get('RIESGO', 'No especificado')}", estilos['Normal']))
    elementos.append(Paragraph(f"<b>Recomendación principal:</b> {diag.get('RECOMENDACION', '')}", estilos['Normal']))
    elementos.append(Spacer(1, 20))
    
    # Respuestas del usuario
    elementos.append(Paragraph("RESPUESTAS PROPORCIONADAS", estilos['Subtitulo']))
    for i, (pregunta, respuesta) in enumerate(respuestas, 1):
        elementos.append(Paragraph(f"{i}. {pregunta}", estilos['Normal']))
        elementos.append(Paragraph(f"<b>Respuesta:</b> {respuesta}", estilos['Normal']))
        elementos.append(Spacer(1, 8))
    
    elementos.append(PageBreak())
    
    # Plan de acción
    elementos.append(Paragraph("PLAN DE ACCIÓN", estilos['Subtitulo']))
    que_hacer = diag.get('QUE_HACER', 'No se proporcionó plan de acción').replace('\n', '<br/>')
    elementos.append(Paragraph(que_hacer, estilos['Normal']))
    elementos.append(Spacer(1, 20))
    
    # Recursos adicionales
    elementos.append(Paragraph("RECURSOS DE APOYO", estilos['Subtitulo']))
    elementos.append(Paragraph("Línea de ayuda psicológica: 0800-222-6464 (Argentina)", estilos['Normal']))
    elementos.append(Paragraph("Guía OMS para manejo de estrés: [www.who.int/mental_health/resources/stress_guide/es/]", estilos['Normal']))
    elementos.append(Paragraph("Ejercicios de respiración guiada: [youtu.be/ejxw-hJf4Fw]", estilos['Normal']))
    
    # Generar PDF
    doc.build(elementos)
    buffer.seek(0)
    return buffer.getvalue()