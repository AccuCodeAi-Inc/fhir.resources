from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DeviceRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Medical device request.
    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """

    __resource_type__ = "DeviceRequest"

    authoredOn: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="authoredOn",
        title="When recorded",
        description="When the request transitioned to being actionable.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_authoredOn", title="Extension field for ``authoredOn``."
    )

    basedOn: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="basedOn",
        title="What request fulfills",
        description="Plan/proposal/order fulfilled by this request.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    codeCodeableConcept: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="codeCodeableConcept",
        title="Device requested",
        description="The details of the device to be used.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e code[x]
            "one_of_many": "code",
            "one_of_many_required": True,
        },
    )

    codeReference: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="codeReference",
        title="Device requested",
        description="The details of the device to be used.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e code[x]
            "one_of_many": "code",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device"],
        },
    )

    context: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="context",
        title="Encounter or Episode motivating request",
        description=(
            "An encounter that provides additional context in which this request is"
            " made."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter", "EpisodeOfCare"],
        },
    )

    definition: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="definition",
        title="Protocol or definition",
        description=(
            "Protocol or definition followed by this request. For example: The "
            "proposed act must be performed if the indicated conditions occur, "
            "e.g.., shortness of breath, SpO2 less than x%."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ActivityDefinition", "PlanDefinition"],
        },
    )

    groupIdentifier: fhirtypes.IdentifierType | None = Field(  # type: ignore
        default=None,
        alias="groupIdentifier",
        title="Identifier of composite request",
        description="Composite request this is part of.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] | None = Field(  # type: ignore
        default=None,
        alias="identifier",
        title="External Request identifier",
        description="Identifiers assigned to this order by the orderer or by the receiver.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    intent: fhirtypes.CodeableConceptType = Field(  # type: ignore
        default=...,
        alias="intent",
        title="proposal | plan | original-order | encoded | reflex-order",
        description=(
            "Whether the request is a proposal, plan, an original order or a reflex"
            " order."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    note: typing.List[fhirtypes.AnnotationType] | None = Field(  # type: ignore
        default=None,
        alias="note",
        title="Notes or comments",
        description=(
            "Details about this request that were not represented at all or "
            "sufficiently in one of the attributes provided in a class. These may "
            "include for example a comment, an instruction, or a note associated "
            "with the statement."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceDateTime: fhirtypes.DateTimeType | None = Field(  # type: ignore
        default=None,
        alias="occurrenceDateTime",
        title="Desired time or schedule for use",
        description=(
            "The timing schedule for the use of the device. The Schedule data type "
            'allows many different expressions, for example. "Every 8 hours"; '
            '"Three times a day"; "1/2 an hour before breakfast for 10 days from '
            '23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".'
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="occurrencePeriod",
        title="Desired time or schedule for use",
        description=(
            "The timing schedule for the use of the device. The Schedule data type "
            'allows many different expressions, for example. "Every 8 hours"; '
            '"Three times a day"; "1/2 an hour before breakfast for 10 days from '
            '23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".'
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    occurrenceTiming: fhirtypes.TimingType | None = Field(  # type: ignore
        default=None,
        alias="occurrenceTiming",
        title="Desired time or schedule for use",
        description=(
            "The timing schedule for the use of the device. The Schedule data type "
            'allows many different expressions, for example. "Every 8 hours"; '
            '"Three times a day"; "1/2 an hour before breakfast for 10 days from '
            '23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".'
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    performer: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="performer",
        title="Requested Filler",
        description="The desired perfomer for doing the diagnostic testing.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "Organization",
                "Patient",
                "Device",
                "RelatedPerson",
                "HealthcareService",
            ],
        },
    )

    performerType: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="performerType",
        title="Fille role",
        description="Desired type of performer for doing the diagnostic testing.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    priorRequest: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="priorRequest",
        title="What request replaces",
        description=(
            "The request takes the place of the referenced completed or terminated "
            "request(s)."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    priority: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="priority",
        title=(
            "Indicates how quickly the {{title}} should be addressed with respect "
            "to other requests"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_priority", title="Extension field for ``priority``."
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="reasonCode",
        title="Coded Reason for request",
        description="Reason or justification for the use of this device.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="reasonReference",
        title="Linked Reason for request",
        description="Reason or justification for the use of this device.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    relevantHistory: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="relevantHistory",
        title="Request provenance",
        description="Key events in the history of the request.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Provenance"],
        },
    )

    requester: fhirtypes.DeviceRequestRequesterType | None = Field(  # type: ignore
        default=None,
        alias="requester",
        title="Who/what is requesting diagnostics",
        description=(
            "The individual who initiated the request and has responsibility for "
            "its activation."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="status",
        title="draft | active | suspended | completed | entered-in-error | cancelled",
        description="The status of the request.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "draft",
                "active",
                "suspended",
                "completed",
                "entered-in-error",
                "cancelled",
            ],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="subject",
        title="Focus of request",
        description="The patient who will use the device.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group", "Location", "Device"],
        },
    )

    supportingInfo: typing.List[fhirtypes.ReferenceType] | None = Field(  # type: ignore
        default=None,
        alias="supportingInfo",
        title="Additional clinical information",
        description=(
            "Additional clinical information about the patient that may influence "
            "the request fulfilment.  For example, this may includes body where on "
            "the subject's the device will be used ( i.e. the target site)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``DeviceRequest`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "definition",
            "basedOn",
            "priorRequest",
            "groupIdentifier",
            "status",
            "intent",
            "priority",
            "codeReference",
            "codeCodeableConcept",
            "subject",
            "context",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "authoredOn",
            "requester",
            "performerType",
            "performer",
            "reasonCode",
            "reasonReference",
            "supportingInfo",
            "note",
            "relevantHistory",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``DeviceRequest`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "identifier",
            "definition",
            "basedOn",
            "priorRequest",
            "groupIdentifier",
            "status",
            "intent",
            "priority",
            "codeReference",
            "codeCodeableConcept",
            "subject",
            "context",
            "occurrenceDateTime",
            "occurrencePeriod",
            "occurrenceTiming",
            "authoredOn",
            "requester",
            "performerType",
            "performer",
            "reasonCode",
            "reasonReference",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "code": ["codeCodeableConcept", "codeReference"],
            "occurrence": [
                "occurrenceDateTime",
                "occurrencePeriod",
                "occurrenceTiming",
            ],
        }
        return one_of_many_fields


class DeviceRequestRequester(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who/what is requesting diagnostics.
    The individual who initiated the request and has responsibility for its
    activation.
    """

    __resource_type__ = "DeviceRequestRequester"

    agent: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="agent",
        title="Individual making the request",
        description="The device, practitioner, etc. who initiated the request.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Device", "Practitioner", "Organization"],
        },
    )

    onBehalfOf: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="onBehalfOf",
        title="Organization agent is acting for",
        description="The organization the device or practitioner was acting on behalf of.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``DeviceRequestRequester`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "agent", "onBehalfOf"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``DeviceRequestRequester`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "agent", "onBehalfOf"]
