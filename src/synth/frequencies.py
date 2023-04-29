def calculate_frequencies(notes):
    """Funktio, joka laskee nuotin nimeä vastaavan taajuuden
    
    Args:
        notes: Lista nuotteja
    
    Returns:
        Palauttaa listan annettuja nuotteja vastaavia taajuuksia
    """
    frequencies = []
    table = {
        "c3": 130.81,
        "c#3": 138.59,
        "d3": 146.83, 
        "d#3": 155.56,
        "e3": 164.81,
        "f3": 174.61,
        "f#3": 185.00,
        "g3": 196.00,
        "g#3": 207.65,
        "a3": 220.00,
        "a#3": 233.08,
        "b3": 246.94,
        "c4": 261.63
    }

    for note in notes:
        frequencies.append(table.get(note))

    return frequencies
