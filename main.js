import axios from 'axios';
import { useState } from 'react';
import './PokerAssistant.css';

const PokerAssistantApp = () => {
  const [currentHand, setCurrentHand] = useState('');
  const [handAnalysisResult, setHandAnalysisResult] = useState('');
  const [handAnalysisHistory, setHandAnalysisHistory] = useState([]);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const analyzePokerHand = async () => {
    setIsAnalyzing(true);
    const apiUrl = `https://api.pokerhands.com/analyze?hand=${currentHand}`;
    try {
      const response = await axios.get(apiUrl);
      setHandAnalysisResult(response.data);
      setHandAnalysisHistory(prevHistory => [...prevHistory, response.data]);
    } catch(error) {
      console.error('Failed to analyze hand:', error);
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="PokerAssistant">
      <input
        value={currentHand}
        onChange={(e) => setCurrentHand(e.target.value)}
        placeholder="Enter hand"
      />
      <button onClick={analyzePokerHand} disabled={isAnalyzing}>
        Analyze Hand
      </button>
      {isAnalyzing ? (
        <div>Loading...</div>
      ) : (
        <div>{handAnalysisResult}</div>
      )}
      <div>
        <h2>Analysis History</h2>
        {handAnalysisHistory.map((result, index) => (
          <div key={index}>{result}</div>
        ))}
      </div>
    </div>
  );
};

export default PokerAssistantApp;