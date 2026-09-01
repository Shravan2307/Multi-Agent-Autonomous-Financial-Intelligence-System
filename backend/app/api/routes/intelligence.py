from fastapi import APIRouter
from pydantic import Field
from app.models import FinalIntelligenceOutput
from app.schemas import FinancialContext, IntelligenceResponse, InvestmentHorizon, PipelineStatus, RiskTolerance, UserProfile, VolatilityTolerance
from app.services.intelligence_pipeline import IntelligencePipeline

router = APIRouter(prefix='/api/intelligence', tags=['intelligence'])

class AnalyzeRequest(FinancialContext):
    user_profile: UserProfile | None = Field(default=None)

def default_profile() -> UserProfile:
    return UserProfile(risk_tolerance=RiskTolerance.MODERATE, investment_horizon=InvestmentHorizon.MEDIUM_TERM, volatility_tolerance=VolatilityTolerance.MEDIUM)

@router.post('/analyze', response_model=IntelligenceResponse)
async def analyze(request: AnalyzeRequest) -> IntelligenceResponse:
    profile = request.user_profile or default_profile()
    context = FinancialContext.model_validate(request.model_dump(exclude={'user_profile'}))
    result: FinalIntelligenceOutput = await IntelligencePipeline().run(symbol=request.symbol, user_profile=profile, context=context)
    return IntelligenceResponse(
        request_id=result.run_id,
        run_id=result.run_id,
        status=PipelineStatus.SUCCESS if result.status == 'COMPLETED' else PipelineStatus.DEGRADED,
        agents=result.agents,
        recommendation=result.recommendation,
        signal=result.signal,
        score=result.score,
        confidence=result.confidence,
        risk_level=result.risk_level,
        profile=result.profile,
        evidence=result.evidence,
        decision_trace=result.decision_trace,
        data_quality=result.data_quality,
    )
