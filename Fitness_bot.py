


while True:
    questions = input("Inserta un aspecto de ti que quieras mejorar (fuerza fisica, resistencia, velocidad, bajar peso, subir peso): ")

    if questions == "fuerza fisica":
        print("Levantamiento de pesas (Enfócate en ejercicios compuestos como el peso muerto, sentadillas y press de banca. "
              "Estos movimientos activan múltiples grupos musculares y son excelentes para aumentar la fuerza máxima). "
              "O Entrenamiento con kettlebells (Movimientos como el swing y el snatch ayudan a mejorar la explosividad y la fuerza general).")

    elif questions == "bajar peso":
        print("Dieta equilibrada, Reducir el consumo de azúcares y carbohidratos refinados, Aumentar la actividad física, "
              "Hidratación adecuada, Dormir bien, Establecer metas realistas, Registrar tus alimentos, "
              "Evitar el comer emocional e Incluye fibra en tu dieta.")

    elif questions == "subir peso":
        print("Ejercicios Compulsivos (Prioriza movimientos compuestos como sentadillas, peso muerto, press de banca y dominadas. "
              "Estos ejercicios trabajan múltiples grupos musculares y son fundamentales para ganar fuerza y masa), Sobrecarga Progresiva "
              "(Aumenta gradualmente el peso que levantas o el número de repeticiones a medida que te vuelves más fuerte. Esto estimula el crecimiento muscular), "
              "Entrenamientos Regulares (Entrena al menos 3-5 veces por semana, asegurándote de incluir días de descanso para permitir la recuperación muscular), "
              "Aumento de Calorías (Consume más calorías de las que quemas. Un superávit de 250-500 calorías al día puede ser un buen punto de partida), "
              "Proteínas (Consume entre 1.6 y 2.2 gramos de proteína por kilogramo de peso corporal al día. Fuentes como carnes magras, pescado, huevos, lácteos, "
              "legumbres y suplementos de proteína son ideales), Carbohidratos y Grasas Saludables (Incluye carbohidratos complejos (avena, arroz integral, patatas) y "
              "grasas saludables (aguacate, nueces, aceite de oliva) para aportar energía y nutrientes), Comidas Frecuentes (Come varias veces al día, incluyendo snacks "
              "saludables entre comidas para asegurar un aporte constante de calorías y nutrientes), Dormir Adecuadamente (Asegúrate de dormir entre 7 y 9 horas cada noche. "
              "El descanso es crucial para la recuperación y el crecimiento muscular), Hidratación (Mantente bien hidratado, ya que el agua es esencial para el rendimiento físico y la recuperación).")

    elif questions == "velocidad":
        print("Realiza sprints cortos (20-100 metros) a máxima intensidad. Descansa adecuadamente entre cada sprint para permitir una recuperación completa. "
              "Incorpora ejercicios explosivos como saltos (saltos en caja, saltos verticales) y lanzamientos de balón medicinal. Esto ayuda a desarrollar la potencia necesaria para aumentar la velocidad. "
              "Practica la técnica de carrera adecuada, centrándote en la postura, el movimiento de los brazos y la zancada. Considera ejercicios de forma como el skipping o los talones a los glúteos. "
              "Alterna períodos de alta intensidad con períodos de descanso o baja intensidad. Por ejemplo, corre a ritmo rápido durante 30 segundos y luego trota durante 1-2 minutos. "
              "Mejora tu fuerza general y específica con ejercicios como sentadillas, peso muerto y press de piernas. Una mayor fuerza en las piernas contribuye a una mayor velocidad. "
              "Realiza estiramientos dinámicos antes de entrenar y estiramientos estáticos después. Mantener una buena movilidad en caderas, tobillos y piernas es esencial para una buena zancada. "
              "Incorpora ejercicios de agilidad como escaleras de agilidad o conos. Estos ejercicios mejoran la rapidez de reacción y la capacidad para cambiar de dirección. "
              "Mejora tu resistencia cardiovascular mediante entrenamientos de larga distancia o trabajos aeróbicos, lo que te ayudará a mantener la velocidad durante más tiempo. "
              "Corre en pendientes o colinas. Esto aumenta la resistencia y fuerza de las piernas, lo que se traduce en una mejor velocidad en terreno llano. "
              "Permite tiempo suficiente para la recuperación entre sesiones de entrenamiento. El descanso es crucial para el desarrollo muscular y la mejora del rendimiento. "
              "Cambia regularmente tus rutinas para evitar la adaptación y seguir desafiando a tu cuerpo.")

    elif questions == "resistencia":
        print("Ejercicios aeróbicos (Realiza actividades como correr, nadar, andar en bicicleta o hacer caminatas rápidas. Intenta mantener una intensidad moderada durante al menos 30 minutos), "
              "Alterna períodos de alta intensidad con períodos de recuperación. Por ejemplo, corre a ritmo rápido durante 1 minuto y luego trota o camina durante 2 minutos. "
              "Esto mejora tanto la resistencia aeróbica como la anaeróbica. Dedica días a ejercicios prolongados, como correr o andar en bicicleta durante 60-120 minutos. "
              "Esto ayuda a aumentar tu capacidad aeróbica y resistencia general. Incorpora levantamiento de pesas y ejercicios de resistencia. Aumentar tu fuerza muscular puede mejorar tu eficiencia "
              "y resistencia en actividades aeróbicas. Realiza ejercicios en circuito que incluyan tanto componentes cardiovasculares como de fuerza. Esto eleva tu ritmo cardíaco y mejora la resistencia. "
              "Incrementa la duración e intensidad de tus entrenamientos poco a poco. Esto ayudará a evitar lesiones y permitirá que tu cuerpo se adapte. Varía tus actividades (correr, nadar, ciclismo, etc.) "
              "para trabajar diferentes grupos musculares y mantener el interés, lo que también ayuda a prevenir el sobreentrenamiento. Realiza ejercicios de alta repetición con pesos ligeros. "
              "Esto ayuda a mejorar la resistencia muscular y la capacidad de tus músculos para trabajar durante más tiempo. Mantente bien hidratado y come alimentos ricos en carbohidratos, proteínas "
              "y grasas saludables. La nutrición adecuada es crucial para el rendimiento y la recuperación. Permite tiempo para que tu cuerpo se recupere. Un buen descanso y sueño son fundamentales para mejorar la resistencia a largo plazo.")

    else:
        print("Opción no válida. Por favor, elige una opción válida.")
    