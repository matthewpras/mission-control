-- Tables for Mission Control V2.1

-- 1. Revenue Tracking
CREATE TABLE IF NOT EXISTS revenue (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at TIMESTAMPTZ DEFAULT now(),
  source TEXT NOT NULL, -- e.g., 'Depop', 'Real Estate', 'Arbitrage'
  amount DECIMAL(10, 2) NOT NULL,
  date DATE DEFAULT CURRENT_DATE,
  notes TEXT
);

-- 2. Project/Arbitrage Leads
CREATE TABLE IF NOT EXISTS leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at TIMESTAMPTZ DEFAULT now(),
  title TEXT NOT NULL,
  status TEXT DEFAULT 'New', -- 'New', 'Researching', 'Active', 'Closed'
  category TEXT, -- 'Real Estate', 'E-commerce', 'Clinical'
  potential_profit DECIMAL(10, 2),
  link TEXT,
  notes TEXT
);

-- 3. Agent Registry
CREATE TABLE IF NOT EXISTS agents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at TIMESTAMPTZ DEFAULT now(),
  agent_id TEXT UNIQUE NOT NULL, -- The readable ID like 'kris-sentinel'
  name TEXT NOT NULL,
  role TEXT,
  status TEXT DEFAULT 'offline', -- 'online', 'busy', 'offline'
  model TEXT,
  last_active TIMESTAMPTZ DEFAULT now(),
  description TEXT,
  capabilities TEXT[], -- array of text
  performance TEXT,
  activity TEXT[] -- array of activity strings
);

-- 4. Tasks Table
CREATE TABLE IF NOT EXISTS tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at TIMESTAMPTZ DEFAULT now(),
  text TEXT NOT NULL,
  status TEXT DEFAULT 'pending', -- 'pending', 'completed'
  link TEXT,
  date DATE DEFAULT CURRENT_DATE
);

-- 5. Board Meetings
CREATE TABLE IF NOT EXISTS board_meetings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at TIMESTAMPTZ DEFAULT now(),
  topic TEXT NOT NULL,
  summary TEXT,
  outcome TEXT,
  agents TEXT[], -- Participating agents
  date DATE DEFAULT CURRENT_DATE
);

-- Enable Realtime for these tables
ALTER PUBLICATION supabase_realtime ADD TABLE revenue;
ALTER PUBLICATION supabase_realtime ADD TABLE leads;
ALTER PUBLICATION supabase_realtime ADD TABLE agents;
ALTER PUBLICATION supabase_realtime ADD TABLE tasks;
ALTER PUBLICATION supabase_realtime ADD TABLE board_meetings;
