from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ToolVersion:
    tool_name: str
    version: str


@dataclass
class HashRecord:
    file_name: str
    algorithm: str
    hash_value: str


@dataclass
class ChainOfCustody:
    evidence_id: str
    collected_by: str
    collection_date: str
    transferred_to: str
    transfer_date: str


@dataclass
class EvidenceItem:
    file_name: str
    file_type: str
    hash_value: str
    metadata: Dict[str, str] = field(default_factory=dict)


@dataclass
class ForensicReport:
    case_name: str
    case_number: str
    examiner: str
    organization: str
    report_date: str
    executive_summary: str
    methodology: str
    findings: List[str] = field(default_factory=list)
    tool_versions: List[ToolVersion] = field(default_factory=list)
    hash_log: List[HashRecord] = field(default_factory=list)
    chain_of_custody: List[ChainOfCustody] = field(default_factory=list)
    evidence_appendix: List[EvidenceItem] = field(default_factory=list)