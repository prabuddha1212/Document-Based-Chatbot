'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function Chat() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      router.push('/login');
    }
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const token = localStorage.getItem('token');
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/chatbot/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ query }),
      });
      if (res.ok) {
        const data = await res.json();
        setResponse(data.response);
      } else {
        setResponse('Query failed');
      }
    } catch (err) {
      setResponse('Query failed');
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-md p-6">
        <h1 className="text-2xl font-bold text-center mb-6">Chat with Documents</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="query" className="block text-sm font-medium text-gray-700">
              Ask a question
            </label>
            <textarea
              id="query"
              name="query"
              rows="4"
              required
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              placeholder="Enter your query..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />
          </div>
          <button
            type="submit"
            disabled={loading}
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
          >
            {loading ? 'Loading...' : 'Ask'}
          </button>
        </form>
        {response && (
          <div className="mt-6">
            <h2 className="text-lg font-medium mb-2">Response</h2>
            <p className="text-gray-700">{response}</p>
          </div>
        )}
      </div>
    </div>
  );
}
