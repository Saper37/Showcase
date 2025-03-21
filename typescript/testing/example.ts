

async function getBotResponse(userInput: string): Promise<string> {
    try {
      const response = await fetch(
        `https://api.openai.com/v1/completions`,
        {
          method: 'POST',
          headers: {
            'Authorization': `Bearer YOUR_API_KEY`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ prompt: userInput, max_tokens: 50 })
        }
      );
      const data = await response.json();
      return data.choices[0].text.trim();
    } catch (error) {
      console.error('Error fetching response:', error);
      return "Sorry, I couldn’t process that.";
    }
  }
